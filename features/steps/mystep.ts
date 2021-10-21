Given ('None', function () {})

When('Benjamin initialise his car with parameters {max_speed}, {horse_power}, and {wheels_list}' ,
    function(max_speed, horse_power, wheels_list, callback){
    // Car creation with given parameters
        let carX = Car(max_speed, horse_power, wheels_list)
            .then(callback)
    })

Then('the car is created',
    function(callback){
    
    })