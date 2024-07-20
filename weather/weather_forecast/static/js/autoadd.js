$(document).ready(function() {
            var currentFocus = -1;

            function addActive(suggestions) {
                if (!suggestions) return false;
                removeActive(suggestions);
                if (currentFocus >= suggestions.length) currentFocus = 0;
                if (currentFocus < 0) currentFocus = (suggestions.length - 1);
                suggestions[currentFocus].classList.add("active");
            }

            function removeActive(suggestions) {
                for (var i = 0; i < suggestions.length; i++) {
                    suggestions[i].classList.remove("active");
                }
            }

            $('#city').on('input', function() {
                var query = $(this).val();
                if (query.length > 0) {
                    $.ajax({
                        url: cityAutocompleteUrl,
                        data: {
                            'q': query
                        },
                        success: function(data) {
                            $('#suggestions').empty();
                            data.forEach(function(city) {
                                $('#suggestions').append('<div class="suggestion">' + city + '</div>');
                            });

                            $('.suggestion').on('click', function() {
                                $('#city').val($(this).text());
                                $('#suggestions').empty();
                                $('#city-form').submit();
                            });
                        }
                    });
                } else {
                    $('#suggestions').empty();
                }
            });

            $('#city').on('keydown', function(e) {
                var suggestions = $('#suggestions').children();
                if (e.keyCode === 40) { 
                    currentFocus++;
                    addActive(suggestions);
                } else if (e.keyCode === 38) { 
                    currentFocus--;
                    addActive(suggestions);
                } else if (e.keyCode === 13) { 
                    e.preventDefault();
                    if (currentFocus > -1) {
                        if (suggestions) suggestions[currentFocus].click();
                    }
                }
            });
        });
