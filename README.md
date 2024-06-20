# car-value-prediction19
python application to evaluate the value of an used car

function addActivity() {
    // Get input values
    var description = document.getElementById('activityDescription').value;
    var duration = parseInt(document.getElementById('activityDuration').value);

    // Validate inputs
    if (!description || isNaN(duration) || duration <= 0) {
        alert('Please provide a valid activity description and a positive duration.');
        return;
    }

    // Add new row to the activity table
    var table = document.getElementById('activityTable').getElementsByTagName('tbody')[0];
    var newRow = table.insertRow();

    var descriptionCell = newRow.insertCell(0);
    var durationCell = newRow.insertCell(1);

    descriptionCell.textContent = description;
    durationCell.textContent = duration;

    // Update total duration
    updateTotalDuration();
