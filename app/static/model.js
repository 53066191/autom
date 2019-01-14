$(function () {

        // jQuery selection for the 2 select boxes
        var dropdown = {
            project_id: $('#select_project'),
            model_id: $('#select_model')
        };

        // call to update on load
        updateModel();

        // function to call XHR and update county dropdown
        function updateModel() {
            var send = {
                project_id: dropdown.project_id.val()
            };
            dropdown.model_id.attr('disabled', 'disabled');
            dropdown.model_id.empty();
            $.getJSON("{{ url_for('api._get_model_by_project') }}", send, function (data) {
                data.forEach(function (item) {
                    dropdown.model_id.append(
                        $('<option>', {
                            value: item[0],
                            text: item[1]
                        })
                    );
                });
                dropdown.model_id.removeAttr('disabled');
            });
        }

        // event listener to state dropdown change
        dropdown.project_id.on('change', function () {
            updateModel();
        });

    });