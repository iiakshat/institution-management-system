document.getElementById('summaryBtn').addEventListener('click', function() {
    document.getElementById('lectureSummary').classList.remove('hidden');
    document.getElementById('lectureNotes').classList.add('hidden');
});

document.getElementById('notesBtn').addEventListener('click', function() {
    document.getElementById('lectureNotes').classList.remove('hidden');
    document.getElementById('lectureSummary').classList.add('hidden');
});
