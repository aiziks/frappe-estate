from ast import Pass
import frappe
from frappe.model.document import Document



class Property(Document):
	pass
	# def after_insert(self):
	# 	frappe.msgprint((f'Document {self.name} inserted successfully! ')) ;
		# frappe.msgprint(__('Document updated successfully'));

	# validating data
	def validate(self):
		doc = frappe.get_doc('Property' , '06-01-2022-Badore Property-00005')
			# doc.discount=9
			# doc.save()
		print(doc)

	

	# 	frappe.msgprint((f'Document {self.name}updated successfully'));
		# pass

		# print(f"\n\n\n {self} \n\n\n")
		# if self.property_type == "Flat":
		# 	for amenity in self.amenities:
		# 		if amenity.amenity == "Outdoor Kitchen":
		# 			frappe.throw(f"Property of type <b>Flat</b> can not have <b>{amenity.amenity}</b> ")

		# sql
		# amenity = frappe.db.sql(f""" select amenity from `tabProperty Amenity` where parent="{self.name}" AND parenttype="Property" and amenity="Outdoor Kitchen"; """ , as_dict=True)
		# print(f"\n\n\n {amenity} \n\n\n")

		# if amenity:
		# 	frappe.throw(f"Property of type <b>Flat</b> can not have <b>{amenity[0].amenity}</b> ")


