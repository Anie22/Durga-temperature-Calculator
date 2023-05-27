function convertTemperature() {
    var temperature = parseFloat($('#temperature').text());
    var fromUnit = $('#from_temp').val();
    var toUnit = $('#to_temp').val();

    $.ajax({
      type: 'GET',
      url: '/convert_temperature/',
      data: {
        temperature: temperature,
        from_unit: fromUnit,
        to_unit: toUnit
      },
      success: function(response) {
        if (response.error) {
          $('#converted').text(response.error);
        } else {
          $('#converted').text(response.converted);
        }
      },
      error: function(xhr) {
        $('#converted').text('Error: ' + xhr.statusText);
      }
    });
  }
  $(document).ready(function() {
    // Convert temperature when digit is entered in input div
    $('#temperature').on('input', function() {
      convertTemperature();
    });

    // Convert temperature when target unit is changed
    $('#to_temp', '#from_temp').change(function() {
      convertTemperature();
    });

    $('.key').click(function() {
      
      convertTemperature();
    });

    // Automatically convert default temperature
    convertTemperature();
  });
  $(document).ready(function() {
    $('#temperature, #from_temp, #to_temp').on('change keyup', function() {
      var temperature = parseFloat($('#temperature').text());
      var from_unit = $('#from_temp').val();
      var to_unit = $('#to_temp').val();

      $.ajax({
        type: 'GET',
        url: '/convert_temperature/',
        data: {
          temperature: temperature,
          from_unit: from_unit,
          to_unit: to_unit
        },
        success: function(response) {
          if (response.error) {
            $('#converted').text(response.error);
          } else {
            $('#converted').text(response.converted);
          }
        },
        error: function(xhr) {
          $('#converted').text('Error: ' + xhr.statusText);
        }
      });
    });
  });