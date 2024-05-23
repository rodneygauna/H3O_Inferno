// Convert UTC timestamps to the browser timezone
// Make sure to add "timestamp" as a class and UTC timestamp to the element as a data attribute
// For example: <td class="timestamp" data-utc="{{ request.created_date.isoformat() }}Z">

// Fetch the UTC timestamp from the element
document.addEventListener("DOMContentLoaded", function() {
    const timestamps = document.querySelectorAll(".timestamp");

    // Convert the UTC timestamp to the browser timezone and format it
    timestamps.forEach((timestampElement) => {
        const utcTimestamp = timestampElement.dataset.utc;
        const browserTimezoneTimestamp = new Date(utcTimestamp).toLocaleString(
            undefined, {
                year: "numeric",
                month: "2-digit",
                day: "2-digit",
                hour: "numeric",
                minute: "numeric",
                hour12: true,
                timeZoneName: "short",
            }
        );

        // Display the formatted local timestamp in the element
        timestampElement.textContent = browserTimezoneTimestamp;
    });
});