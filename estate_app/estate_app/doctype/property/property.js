// Copyright (c) 2022, isaca and contributors
// For license information, please see license.txt

frappe.ui.form.on('Property', {

	setup:  frm => {

		frm.check_amenity_duplicate = (frm , row) => {
			frm.doc.amenities.forEach(item => {

				if(row.amenity == '' || row.idx == item.idx ){
					// do nothing 
				}else{
				if ( row.amenity == item.amenity ){

					// since the row has been generated already we will assign a blank value to it
					row.amenity = ''
					frm.refresh_field('amenities')
					frappe.throw(__(`${row.amenity} already exist in row ${item.idx}`))
					
				}
			}
			})
		}

		// check flat against outdoor kitchen
		frm.check_flat_against_outdoor_kitchen = (frm ,row) => {
			
			if( row.amenity=='Outdoor Kitchen' && frm.doc.property_type == 'Flat'){
				let amenity = row.amenity
				row.amenity = ''
				frm.refresh_field('amenities')
				frappe.throw(__(`${amenity} must not be in a flat `))
				
			}
			
		}

		frm.compute_total = (frm) => {
			console.log('Property price ',frm.doc.property_price)
			let total = 0;
			// looping through the child table
			frm.doc.amenities.forEach(amenity => {
				total = total + amenity.amenity_price
			})

			// new total
			let new__total = frm.doc.property_price + total;
			if(frm.doc.discount){
				new__total = new__total - (new__total* (frm.doc.discount/100))
			}

			console.log(new__total)
			frm.set_value('grand_total' , new__total);
		}

		// copying discount to property_amenity
		frm.copy_discount = (frm) =>{
			frm.doc.amenities.forEach(item => {
				item.discount = frm.doc.discount
			})
			frm.refresh_field('amenities')
		} 

	},



	// refresh event
	refresh: (frm) => {
		frm.add_custom_button("Say Hello" , () => {
			frappe.prompt("Address" , ({value}) =>{
				if(value){
					frm.set_value("address" , value)
					frm.refresh_field('address')
					frappe.msgprint((`Address field updated with ${value} `))
				}
			})
		}, "Actions" );


		// check property types  ;  WE USE THE BUTTON TO MAKE AJAX CALL TO API ENDPOINT
		frm.add_custom_button('Check Property Types' , () => {
			let property_type = frm.doc.property_type 
			// console.log(property_type);

			// making ajax call
			frappe.call({
				method: "estate_app.estate_app.doctype.property.api.check_property_types",
				args : {"property_type": property_type },
				callback : (r) => {
					console.log(r)
					if (r.message.length>0){
						let header = `<h3> Below properties is of type ${property_type} </h3>`;
						let body = ``;
						r.message.forEach(d => {
							let cont = `<p>Name: ${d.name} : <a href="/app/property/${d.name}" target="_blank"> Visit </a></p>`
							body += cont;
						})

						let all = header + body
						frappe.msgprint(__(all))

					}
					
				}
			})

		} , "Actions" )

	},



	// total recompute immediately property_price filed changes
	property_price: (frm) => {
		frm.compute_total(frm )
	},

	// total recompute immediately discount field changes
	discount :  (frm) => {
		frm.copy_discount(frm) 
		frm.compute_total(frm )
	}
		

});



frappe.ui.form.on('Property Amenity' , {

	amenity : (frm , cdt , cdn) => {

		let row = locals[cdt][cdn]
		// console.log(row)
		// console.log('Printed the child doctype row object')
		frm.check_amenity_duplicate(frm , row)
		frm.check_flat_against_outdoor_kitchen( frm , row )
		frm.compute_total(frm)

	},
	

	amenities_remove : (frm , cdt, cdn ) => {
		frm.compute_total(frm)
	}

})