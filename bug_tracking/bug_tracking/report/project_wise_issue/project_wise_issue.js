// Copyright (c) 2024, Sanskar Technolab and contributors
// For license information, please see license.txt

frappe.query_reports["Project Wise Issue"] = {
	"filters": [
		{
			fieldname: "project",
			label: "Project",
			fieldtype: "Link",
			options: "Project",
		},
		{
			fieldname: "from_date",
			label: "From Date",
			fieldtype: "Date",
		},
		{
			fieldname: "to_date",
			label: "To Date",
			fieldtype: "Date",
		},
		{
			fieldname: "is_bug",
			label: "Is Bug",
			fieldtype: "Check",
			default: 0
		}
	]
};
