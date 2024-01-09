// Copyright (c) 2024, Sanskar Technolab and contributors
// For license information, please see license.txt

frappe.query_reports["User Wise Issue"] = {
	"filters": [
		{
			fieldname: "user",
			label: __("User"),
			fieldtype: "Link",
			options: "User",
		}
	]
};
