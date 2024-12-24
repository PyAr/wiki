document.addEventListener('DOMContentLoaded', function() {
    var searchIndex = new FlexSearch.Index();  // Initialize FlexSearch
    var index = {};  // This will store the index data globally within this script block

    // Fetch the generated JSON file
    fetch('/wiki/search_index.json')
    .then(response => response.json())
    .then(data => {
        index = data;  // Store the fetched data in the 'index' variable
        for (var key in index) {
            if (index.hasOwnProperty(key)) {
                searchIndex.add(key, index[key].content);
            }
        }
    });

    var input = document.getElementById('search_input');
    var button = document.getElementById('search_button');

    // Function to perform search
    function performSearch() {
        var query = input.value;
        var results = searchIndex.search(query);
        var resultsContainer = document.getElementById('search_results');
        resultsContainer.innerHTML = ''; // Clear previous results

        var ul = document.createElement('ul'); // Create a UL element to hold the results

        // Display results
        results.forEach(function(result) {
            var li = document.createElement('li'); // Create a LI element for each result
            var link = document.createElement('a');
            link.href = index[result].url;
            link.textContent = index[result].title;
            li.appendChild(link);
            ul.appendChild(li); // Append the LI to the UL
        });

        resultsContainer.appendChild(ul); // Append the UL to the results container
        document.getElementById('search_overlay').style.display = 'flex'; // Show the overlay
    }

    // Event listener for search button click
    button.addEventListener('click', performSearch);

    // Event listener for pressing enter key in the search input
    input.addEventListener('keypress', function(event) {
        if (event.key === "Enter" || event.keyCode === 13) {
            event.preventDefault();  // Prevent the form from being submitted
            performSearch();
        }
    });
});

// Function to close the search overlay
function closeSearch() {
    document.getElementById('search_overlay').style.display = 'none';
}

document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape') {
        var searchOverlay = document.getElementById('search_overlay');
        if (searchOverlay !== null) {
            closeSearch();
        }
    }
});