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

    // Clear input fields
    document.getElementById('activityDescription').value = '';
    document.getElementById('activityDuration').value = '';
}

function updateTotalDuration() {
    var table = document.getElementById('activityTable').getElementsByTagName('tbody')[0];
    var rows = table.getElementsByTagName('tr');
    var totalDuration = 0;

    for (var i = 0; i < rows.length; i++) {
        var duration = parseInt(rows[i].getElementsByTagName('td')[1].textContent);
        totalDuration += duration;
    }

    document.getElementById('totalDuration').textContent = 'Total Duration: ' + totalDuration + ' minutes';
}
