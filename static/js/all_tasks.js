(function () {
    var prioritySelect = document.getElementById("priority");
    if (!prioritySelect) {
        return;
    }

    function applyPriorityColor() {
        var option = prioritySelect.options[prioritySelect.selectedIndex];
        var color = option.getAttribute("data-color") || "#ff8a80";
        prioritySelect.style.backgroundColor = color;
        prioritySelect.style.color = "#111827";
    }

    prioritySelect.addEventListener("change", applyPriorityColor);
    applyPriorityColor();
})();
