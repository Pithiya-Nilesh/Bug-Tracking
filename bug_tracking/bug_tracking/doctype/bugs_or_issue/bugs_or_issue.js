// Copyright (c) 2024, Sanskar Technolab and contributors
// For license information, please see license.txt

frappe.ui.form.on('Bugs or Issue', {
    refresh: function(frm) {
        // Trigger the calculation when the form is loaded
        calculateTimeDifference(frm);
    },
    
    reported_on: function(frm) {
        // Trigger the calculation when the start_datetime field changes
        calculateTimeDifference(frm);
    },
    
    resolved_on: function(frm) {
        // Trigger the calculation when the end_datetime field changes
        calculateTimeDifference(frm);
    }
});

function calculateTimeDifference(frm) {
    var startDatetime = frm.doc.reported_on;
    var endDatetime = frm.doc.resolved_on;

    if (startDatetime && endDatetime) {
        // Convert date strings to Date objects
        var startDate = new Date(startDatetime);
        var endDate = new Date(endDatetime);

        // Calculate the time difference in milliseconds
        var timeDifference = endDate - startDate;

        // Convert milliseconds to seconds
        var secondsDifference = timeDifference / 1000;
        frm.set_value('resolved_time', secondsDifference);
    }
}
