// Copyright (c) 2024, Sanskar Technolab and contributors
// For license information, please see license.txt

frappe.query_reports["User Wise Bug"] = {
	"filters": [{
		fieldname: "user",
		label: __("User"),
		fieldtype: "Link",
		options: "User",
	},
	{
		fieldname: "bug_type",
		label: "Bug Type",
		fieldtype: "Link",
		options: "Bug Type",
	},
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
		default: 1
	},
	{
		fieldname: "group_by",
		label: "Group By",
		fieldtype: "Select",
		options: "Project\nUser",
		default: "Project"
	}

	]
};
