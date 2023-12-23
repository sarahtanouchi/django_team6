

function setupTeaFilterOptions() {
    const form = document.getElementById("filter_items_form");
    console.log(form);
    
    const teaTypeFilterCheckboxes = form.querySelectorAll("input[name=tea_type_filter]");
    console.log(teaTypeFilterCheckboxes)
    
    const searchParams = new URLSearchParams(window.location.href);
    // for (const [key,value] of searchParams) {
    //     console.log(key, value);
    // }
    if (searchParams.has("tea_type_filter")) {
        const usedFilterOptions = searchParams.getAll("tea_type_filter");
        for (const checkbox of teaTypeFilterCheckboxes) {
            console.log(checkbox.value)
            const checked = usedFilterOptions.includes(checkbox.value);
            console.log("Checked? ", checked, checkbox)
            checkbox.checked = checked;
        }
    }
}

setupTeaFilterOptions()