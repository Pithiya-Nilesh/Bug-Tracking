# Copyright (c) 2024, Sanskar Technolab and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
	
	columns = [
		{
			"label": "Project",
			"options": "Project",
			"fieldname": "project",
			"fieldtype": "Link",
			"width": 200,
		},
		{
			"label": "Open",
			"fieldname": "open",
			"fieldtype": "Data",
			"width": 100,
		},
		{
			"label": "Working",
			"fieldname": "working",
			"fieldtype": "Data",
			"width": 100,
		},
		{
			"label": "Pending Review",
			"fieldname": "pending_review",
			"fieldtype": "Data",
			"width": 100,
		},
		{
			"label": "Overdue",
			"fieldname": "overdue",
			"fieldtype": "Data",
			"width": 100,
		},
		{
			"label": "Completed",
			"fieldname": "completed",
			"fieldtype": "Data",
			"width": 100,
		},
		{
			"label": "Cancelled",
			"fieldname": "cancelled",
			"fieldtype": "Data",
			"width": 100,
		},
		{
			"label": "Total Task",
			"fieldname": "total_task",
			"fieldtype": "Data",
			"width": 100,
		},
	]

	data = get_data(filters)

	if filters.project and data:
		chart_data = data[0]
		chart = {
			'type': 'donut', 
			'data': {
				'labels': ["Open", "Working", "Pending Review", "Overdue", "Completed", "Cancelled", "Total Task"], 
				'datasets': [{'values': [chart_data["open"], chart_data["working"], chart_data["pending_review"], chart_data["overdue"], chart_data["completed"], chart_data["cancelled"]]}]}}
		
		# task = [{
		# "value": chart_data["total_task"],
		# "indicator": "green" if chart_data["total_task"] > 0 else "red",
		# "label": "Total Task",
		# },

		# {
		# "value": chart_data["total_task"],
		# "indicator": "green" if chart_data["total_task"] > 0 else "red",
		# "label": "Total Revenue",
		# "datatype": "Currency",
		# }]
		
		# return columns, data, None, chart, task

		return columns, data, None, chart
	
	else:
		chart = {
			'type': 'donut', 
			'data': {
				'labels': [row["project"] for row in data],
				'datasets': [{
					'values': [row["total_task"] for row in data]
				}]
			}
		}
		
		return columns, data, None, chart

# def get_data(filters):
# 	sql = f"""
# 		SELECT project, count(name) as total_task, 
# 		SUM(CASE WHEN status = 'Open' THEN 1 ELSE 0 END) AS open,
#     	SUM(CASE WHEN status = 'Working' THEN 1 ELSE 0 END) AS working,
# 		SUM(CASE WHEN status = 'Pending Review' THEN 1 ELSE 0 END) AS pending_review,
# 		SUM(CASE WHEN status = 'Overdue' THEN 1 ELSE 0 END) AS overdue,
# 		SUM(CASE WHEN status = 'Completed' THEN 1 ELSE 0 END) AS completed,
# 		SUM(CASE WHEN status = 'Cancelled' THEN 1 ELSE 0 END) AS cancelled
# 		FROM `tabTask`
# 		"""
	
	
# 	if filters.project:
# 		sql += f" WHERE project = '{filters.project}'"

# 	sql += " GROUP BY project"
	
# 	return frappe.db.sql(sql, as_dict=True)
	

def get_data(filters, user=frappe.session.user):
	# Check permission to access 'tabTask'
	
	sql = """
		SELECT project, count(name) as total_task, 
		SUM(CASE WHEN status = 'Open' THEN 1 ELSE 0 END) AS open,
		SUM(CASE WHEN status = 'Working' THEN 1 ELSE 0 END) AS working,
		SUM(CASE WHEN status = 'Pending Review' THEN 1 ELSE 0 END) AS pending_review,
		SUM(CASE WHEN status = 'Overdue' THEN 1 ELSE 0 END) AS overdue,
		SUM(CASE WHEN status = 'Completed' THEN 1 ELSE 0 END) AS completed,
		SUM(CASE WHEN status = 'Cancelled' THEN 1 ELSE 0 END) AS cancelled
		FROM `tabTask`
	"""

	if filters.project:
		sql += f" WHERE project = '{filters.project}'"

	sql += " GROUP BY project"

	# # Retrieve the list of projects that the user has permission to access
	# allowed_projects = frappe.get_all('User Permission', filters={'user': user, 'allow': "Project"}, fields=['for_value'], pluck='for_value')
		
	# # Filter the result to include only allowed projects
	# result = [item for item in frappe.db.sql(sql, as_dict=True, debug=0) if item['project'] in allowed_projects]

	allowed_customers = frappe.get_all('User Permission', filters={'user': user, 'allow': "Customer"}, fields=['for_value'], pluck='for_value')
	result = [item for item in frappe.db.sql(sql, as_dict=True, debug=0) if item['customer'] in allowed_customers]

	return result
