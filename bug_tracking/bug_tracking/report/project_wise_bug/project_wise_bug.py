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
			"label": "Total Issue",
			"fieldname": "total_issue",
			"fieldtype": "Data",
			"width": 200,
		}
	]
	
	columns, data = get_data(filters, columns)

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
		SELECT custom_assigned_to as user, project, customer, count(name) as total_issue 
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

	return columns , frappe.db.sql(sql, as_dict=True)
