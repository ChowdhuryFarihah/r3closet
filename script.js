const tagShown = new Map();




function showTagsTable() {
    const tags = document.getElementsByClassName("tag");
    const table = document.getElementById("tags-table");
    table.style.backgroundColor = "rgb(248, 56, 91)";
    for (const tag of tags) {
        tag.style.display = "block";
        tagShown.set(tag, false);
        tag.addEventListener("click", function(event) {
            const clickedElement = event.target;
            if (tagShown.get(clickedElement) == false) {
                clickedElement.style.backgroundColor = "red";
                tagShown.set(clickedElement, true);
            }
            else {
                clickedElement.style.backgroundColor = "rgb(241, 185, 215)";
                tagShown.set(clickedElement, false);
            }
        })
        console.log(tagShown);
    }
}

function submitTags() {
    const tags = [];
    for (const tag of tagsShown) {
        if (tagShown.get(tag) == true) {
            tags.push(tag.text);
        }

    }
    const tagsTable = document.getElementById("tags-table");
    tagsTable.style.display = "none";
    fetch('/submitTags', {
        method: 'POST',
        headers: {
            'Content-type': 'application/json'
        },
        body: JSON.stringify(tags)
    })

}