// Basado en https://plugins.getnikola.com/#flexsearch_plugin

document.addEventListener('DOMContentLoaded', function() {
    var searchIndex = new FlexSearch.Index();  // Initialize FlexSearch
    var index = {};  // This will store the index data globally within this script block

    // Fetch the generated JSON file
    const basePath = "" //document.location.hostname == "localhost" ? "": "/wiki" //Parche para probar en las GHP de mi fork ak.saxa.xyz/wiki
    var indexPath = document.location.origin + basePath + "/search_index.json"
    fetch(indexPath)
    .then(response => response.json())
    .then(data => {
        index = data;  // Store the fetched data in the 'index' variable
        for (var key in index) {
            if (index.hasOwnProperty(key)) {
                searchIndex.add(key, index[key].content);
            }
        }
    });

    var inputBase = document.getElementById('search_input_base');
    var input = document.getElementById('search_input');

    // Function to perform search
    function performSearch() {
        var query = input.value;
  
        var results = searchIndex.search(query);
        var resultsContainer = document.getElementById('search_results');
        resultsContainer.innerHTML = ''; // Clear previous results

        var resultsCount = document.getElementById('search_count');
        resultsCount.innerHTML = results.length + " resultado(s)";
        
        if (input.value === ""){
            return
        }

        var ul = document.createElement('ul'); // Create a UL element to hold the results

        // Display results
        results.forEach(function(result) {
            var li = document.createElement('li'); // Create a LI element for each result
            var link = document.createElement('a');
            link.href = basePath + index[result].url;
            link.textContent = index[result].title;
            li.appendChild(link);
            ul.appendChild(li); // Append the LI to the UL
        });

        resultsContainer.appendChild(ul); // Append the UL to the results container
    }

    inputBase.addEventListener('click', ()=>{
        document.getElementById('search_overlay').style.display = 'flex'; // Show the overlay
        inputBase.disabled = true;
        input.focus();
    })

    // Event listener for each change in the input field 
    input.addEventListener('input', performSearch);

// Function to close the search overlay
    function closeSearch() {
        document.getElementById('search_overlay').style.display = 'none';
        document.getElementById('search_input_base').disabled = false;
        document.getElementById('search_input').value === ""
    }

    document.addEventListener('keydown', function(event) {
        if (event.key === 'Escape') {
            var searchOverlay = document.getElementById('search_overlay');
            if (searchOverlay !== null) {
                closeSearch();
            }
        }
    });
});


