const urlParams = new URL(window.location.href).searchParams;
const selectedFilters = new Map();
for (const key of urlParams.keys()) {
    const filterValues = urlParams.getAll(key);
    selectedFilters.set(key, filterValues);
}

function createCheckboxGroup(containerId, name) {
    const form = document.getElementById(containerId);
    const allCheckboxes = Array.from(form.querySelectorAll(`input[name=${name}]`));

    const allOption = allCheckboxes.find(x => x.value == 'all');
    const otherOptions = allOption ? allCheckboxes.filter(x => x != allOption) : allCheckboxes;

    const checkAllOptionsSelected = (e) => {
        const allChecked = !otherOptions.some(x => !x.checked);
        allOption.checked = allChecked;
    };

    if (allOption) {
        for (const checkbox of otherOptions)
            checkbox.addEventListener('change', checkAllOptionsSelected);
        
        allOption.addEventListener('change', (e) => {
            for (const checkbox of otherOptions) {
                checkbox.removeEventListener('change', checkAllOptionsSelected);
                checkbox.checked = e.target.checked;
                checkbox.addEventListener('change', checkAllOptionsSelected);
            }
        });
    }
        
    return { allCheckbox: allOption, otherOptions };
}

function autoTickCheckboxes(checkboxes) {
    for (const checkbox of checkboxes) {
        const checked = selectedFilters.get(checkbox.name)?.includes(checkbox.value) ?? false;
        checkbox.checked = checked;
        checkbox.dispatchEvent(new Event('change'));
    }
}

function setupFilterCheckboxes() {
    const formId = 'filter_items_form';
    const teaTypeCheckboxes = createCheckboxGroup(formId, 'tea_type_filter');
    const teaSetTypeCheckboxes = createCheckboxGroup(formId, 'tea_set_type_filter');
    const tasteCheckboxes = createCheckboxGroup(formId, 'taste_filter');
    const occassionCheckboxes = createCheckboxGroup(formId, 'occasion_filter');
    const priceCheckboxes = createCheckboxGroup(formId, 'price_filter');
    const itemTypeCheckboxes = createCheckboxGroup(formId, 'item_type_filter');

    autoTickCheckboxes(teaTypeCheckboxes.otherOptions);
    autoTickCheckboxes(teaSetTypeCheckboxes.otherOptions);
    autoTickCheckboxes(tasteCheckboxes.otherOptions);
    autoTickCheckboxes(occassionCheckboxes.otherOptions);
    autoTickCheckboxes(priceCheckboxes.otherOptions);
    autoTickCheckboxes(itemTypeCheckboxes.otherOptions);
}

// page finished loading, run the setup filter checkboxes function
document.addEventListener('DOMContentLoaded', setupFilterCheckboxes);