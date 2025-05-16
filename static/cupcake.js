/**
 * cupcake.js
 * -----------
 * Handles cupcake form submission and image styling for the Cupcake app.
 * 
 * - Sets a fixed width for all images on the page.
 * - Submits new cupcake data to the backend API using AJAX (axios).
 * - Resets the form after successful submission.
 * 
 * Dependencies:
 *   - jQuery
 *   - Axios
 */

$(document).ready(function () {

    // sets all images to a fixed width for consistent layout
    const images = document.querySelectorAll("img")
    for (let img of images) {
        img.style.width = "200px";
    }


    /**
     * Handle cupcake form submission.
     * Prevents default form behavior, collects form data,
     * sends a POST request to the API, and resets the form.
     */
    $("#cupcake_form").on("submit", async function (evt) {
        evt.preventDefault();

        // Store form vlaues
        let flavor = $("#form_flavor").val();
        let size = $("#form_size").val();
        let rating = $("#form_rating").val();
        let image = $("#form_image").val();

        // Send a POST request to create a new cupcake
        const newCupcakePost = await axios.post(`/api/cupcakes`, { flavor, size, rating, image });

        // Reset the form fields after submission
        $("#cupcake_form").trigger("reset");
    });

});

