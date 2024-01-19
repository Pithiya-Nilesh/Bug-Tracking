# Copyright (c) 2024, Sanskar Technolab and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
	columns, data = [], []
	
	columns = [
		{
			"label": "Project",
			"options": "Project",
			"fieldname": "project",
			"fieldtype": "Link",
			"width": 200,
		},
		{
			"label": "Customer",
			"fieldname": "customer",
			"options": "Customer",
			"fieldtype": "Link",
			"width": 200,
		},
		{
			"label": "Open Issue",
			"fieldname": "open_issues",
			"fieldtype": "Data",
			"width": 100,
		},
		{
			"label": "Closed Issue",
			"fieldname": "closed_issues",
			"fieldtype": "Data",
			"width": 125,
		},
		{
			"label": "Resolved Issue",
			"fieldname": "resolved_issues",
			"fieldtype": "Data",
			"width": 125,
		},
		{
			"label": "On Hold Issue",
			"fieldname": "on_hold_issues",
			"fieldtype": "Data",
			"width": 125,
		},
		{
			"label": "Replied Issue",
			"fieldname": "replied_issues",
			"fieldtype": "Data",
			"width": 125,
		},
		{
			"label": "Total Issue",
			"fieldname": "total_issue",
			"fieldtype": "Data",
			"width": 100,
		}

	]
	
	columns, data = get_data(filters, columns)

	if filters.project and data:
		chart_data = data[0]
		chart = {
			'type': 'donut', 
			'data': {
				'labels': ["Open", "Closed", "Resolved", "On Hold", "Replied"], 
				'datasets': [{'values': [chart_data["open_issues"], chart_data["closed_issues"], chart_data["resolved_issues"], chart_data["on_hold_issues"], chart_data["replied_issues"]]}]}}
		
		return columns, data, None, chart
	
	else:
		chart = {
			"type": "donut",
			"data": {
				"labels": [row["project"] for row in data],
				"datasets": [
					{
						"values": [row["total_issue"] for row in data]
					}
				]
			}
		}
		return columns, data, None, chart

def get_data(filters, columns):
	
	sql = """
		SELECT custom_assigned_to as user, project, customer, count(name) as total_issue, 
		SUM(CASE WHEN status = 'Open' THEN 1 ELSE 0 END) AS open_issues,
    	SUM(CASE WHEN status = 'Closed' THEN 1 ELSE 0 END) AS closed_issues,
		SUM(CASE WHEN status = 'Resolved' THEN 1 ELSE 0 END) AS resolved_issues,
		SUM(CASE WHEN status = 'On Hold' THEN 1 ELSE 0 END) AS on_hold_issues,
		SUM(CASE WHEN status = 'Replied' THEN 1 ELSE 0 END) AS replied_issues
		FROM `tabIssue`
		WHERE docstatus=0
		"""
	
	if filters.user:
		sql += f" and custom_assigned_to = '{filters.user}'"
		columns.append({
			"label": "User",
			"options": "User",
			"fieldname": "user",
			"fieldtype": "Link",
			"width": 200,
		},)

	if filters.project:
		sql += f" and project = '{filters.project}'"

	if filters.bug_type:
		sql += f" and custom_bug_type = '{filters.bug_type}'"

	if filters.is_bug:
		sql += f" and custom_is_bug={filters.is_bug}"

	if filters.from_date and filters.to_date:
		from datetime import datetime

		input_date = datetime.strptime(filters.from_date, "%Y-%m-%d")
		from_date = input_date.strftime("%Y-%m-%d %H:%M:%S.%f")	

		to_date1 = datetime.strptime(filters.to_date, "%Y-%m-%d")
		to_date = to_date1.strftime("%Y-%m-%d %H:%M:%S.%f")

		sql += f" and creation BETWEEN '{from_date}' AND '{to_date}'"
	
	sql += " GROUP BY project"

	# Retrieve the list of projects that the user has permission to access
	allowed_projects = frappe.get_all('User Permission', filters={'user': frappe.session.user, 'allow': "Project"}, fields=['for_value'], pluck='for_value')
		
	# Filter the result to include only allowed projects
	result = [item for item in frappe.db.sql(sql, as_dict=True, debug=0) if item['project'] in allowed_projects]

	return columns, result

