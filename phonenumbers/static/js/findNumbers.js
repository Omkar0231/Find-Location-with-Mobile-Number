let phone_number_input = $('#phone-number')
let user_text = $('#user-text')

phone_number_input.on('input', function(){
    $('.find-number-row table tbody td').empty()
})

user_text.on('input', function(){
    $('.mobile-numbers-table tbody').empty()
})


$('#phone-number-form').on('submit', function(event){
    event.preventDefault()
    $.ajax({
        url: '/mobile-numbers/find-number-api/',
        type: 'POST',
        data: {
            'number': phone_number_input.val()
        },
        success: function(data){
            console.log('API Hit Successfully :: ', data)
            let tbody = $('.find-number-row table tbody')

            tbody.find('.country-code').text(data.country_code)
            tbody.find('.mobile-number').text(data.mobile_number)
            tbody.find('.country').text(data.country)
            tbody.find('.service-provider').text(data.service_provider)
            tbody.find('.timezone').text(data.timezone)
        },
        error: function(err){
            console.log('Error Message :: ', err)
            alert(err.responseJSON[0])

        }
    })
})


$('#find-phone-numbers-form').on('submit', function(event){
    event.preventDefault()
    $.ajax({
        url: '/mobile-numbers/find-numbers-in-text-api/',
        type: 'POST',
        data: {
            'text': user_text.val()
        },
        success: function(data){
            console.log('API Hit Successfully :: ', data)
            let tbody = $('.mobile-numbers-table tbody')
            tbody.empty()
           $.each(data.mobile_numbers, function(index, number){
                tbody.append(
                    `<tr>
                        <td>${index + 1}</td>
                        <td>${number}</td>
                    </tr>`
                )
           })
        },
        error: function(err){
            console.log('Error Message :: ', err)
            alert(err.responseJSON[0])

        }
    })
})