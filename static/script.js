const searchInput = document.querySelector("[data-search]")
const searchButton = document.querySelector("[search-button]")
const li_elements = document.getElementById("domains-list").getElementsByTagName("li")
const ul = document.getElementById("domains-list")

searchButton.disabled=true

searchInput.addEventListener("input",e => {
    const value = e.target.value
    searchButton.disabled=true

    for(let i = 0; i < li_elements.length;i++){
        const s = li_elements[i].textContent
        var isVisible = s.toLowerCase().includes(value.toLowerCase())
        
        if(isVisible === false) {
            li_elements[i].style.display = "none"
        } else {
            li_elements[i].style.display = "block"
        }
    } 
})

ul.addEventListener("click",e => {
    const value = e.target
    searchInput.value = value.textContent
    searchButton.disabled=false

})

