$(document).ready(function () {
  var isNegative = false;
  var mainInput = '0';

  $('#temperature, #from_temp, #to_temp').on('change keyup', function() {
    mainInput = $('#temperature').text();
    convertTemperature();
  });

  $('#to_temp', '#from_temp').change(function() {
    convertTemperature();
  });

  function convertTemperature () {
    var temperature = parseFloat($('#temperature').text().replace(/,/g, ''));
    var fromUnit = $('#from_temp').val();
    var toUnit = $('#to_temp').val();

    $.ajax({
      type: 'GET',
      url: '/convert_temperature',
      data: {
        temperature: temperature,
        from_unit: fromUnit,
        to_unit: toUnit
      },
      success: function(response) {
        if (response.error) {
          $('#converted').text(response.error);
        } else {
          var resultValueWithCommas = response.converted.toLocaleString();
          $('#converted').text(resultValueWithCommas);
        }
      }
    })
  }

  function updateTemperatureDisplay () {
    var fontSize = 55;
    var minFontSize = 30.1
  
    let calculatedFontSize = fontSize - (mainInput.length - 2) * 2;
    calculatedFontSize = Math.max(calculatedFontSize, minFontSize)
    $('.temp_value, .result').css('font-size', calculatedFontSize + 'px');

    $('#temperature').text(mainInput);
  }

  function resetTemperatureFontSize() {
    var fontSize = 55;
    var minFontSize = 30.1
  
    let calculatedFontSize = minFontSize + (mainInput.length - 2);
    calculatedFontSize = Math.max(calculatedFontSize, fontSize)
    $('.temp_value, .result').css('font-size', calculatedFontSize + 'px');
  }

  function updateTemperatureSign() {
    var currentTemperature = $('#temperature').text();
    if (isNegative) {
      $('#temperature').text('-' + currentTemperature);
    }else{
      $('#temperature').text(currentTemperature.replace('-', ''))
    }
  }

  $('.key').click(function() {
    var clickedNumber = $(this).text();
    let hasDecimal = mainInput.toLowerCase().search(".");
    if(mainInput.length < 15){
      
      if (mainInput === "0") {
        mainInput = clickedNumber;
      } else {
        mainInput += clickedNumber;
      }
    
      if (hasDecimal || mainInput.indexOf(".") === -1) {
        // Add commas as thousands separator but not to the numbers after the decimal point
        mainInput = mainInput.replace(/,/g, '');
        mainInput = mainInput.replace(/\B(?=(\d{3})+(?!\d))/g, ",");
      }

      updateTemperatureDisplay();
      convertTemperature();
    }
  });

  $('.del-key').click(function() {
    // Handle deleting the last character
    if (mainInput.length > 1) {
      mainInput = mainInput.substring(0, mainInput.length - 1);
  
      // Only add commas as thousands separator if there is no decimal
      // if (!hasDecimal) {
      //   mainInput = mainInput.replace(/\B(?=(\d{3})+(?!\d))/g, ",");
      // }
  
      // Remove any commas after the decimal point
      mainInput = mainInput.replace(/,\B(?=\d)/g, '');
    } else {
      mainInput = "0";
    }
  
    updateTemperatureDisplay();
  });

  $('.minus').click(function() {
    if (!isNegative) {
      isNegative = true;
      updateTemperatureSign();
      convertTemperature();
    }
  });

  $('.plus').click(function() {
    isNegative = false;
    updateTemperatureSign();
    convertTemperature();
  });

  $('.del-all-key').click(function() {
    $('#temperature').text('0');
    mainInput = "";
    convertTemperature();
    resetTemperatureFontSize(); 
  });
  convertTemperature();
})
    