// Stripe JS for credit card element

const stripePublicKey = document.getElementById("id_stripe_public_key").textContent.slice(1, -1)
const clientSecret = document.getElementById("id_client_secret").textContent.slice(1, -1)
const errorDiv = document.getElementById("card-errors")
const form = document.getElementById("payment-form")
const paymentButton = document.getElementById("submit-payment-button")
const saveInfoCheck = document.getElementById("id-save-info")
const csrfTokenInput = document.getElementsByName("csrfmiddlewaretoken")
let stripe = Stripe(stripePublicKey)
let elements = stripe.elements()
let card = elements.create("card")
card.mount("#card-element")

card.addEventListener('change', e => {
    if (e.error) {
        errorDiv.innerHTML = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${e.error.message}</span>
        `
    } else {
        errorDiv.textContent = ""
    }
})

form.addEventListener("submit", e => {
    e.preventDefault()
    card.update({
        "disabled": true
    })
    paymentButton.setAttribute("disabled", "")
    let saveInfo = Boolean(saveInfoCheck.checked)
    let csrfToken = csrfTokenInput[0].value
    let postData = new FormData()
    postData.append("csrfmiddlewaretoken", csrfToken)
    postData.append("client_secret", clientSecret)
    postData.append("save_info", saveInfo)
    let url = "cache_checkout_data/"

    fetch(url, {
        method: "POST",
        credentials: "same-origin",
        body: postData,
        headers: {
            "X-CSRFToken": csrfToken
        }
    }).then(response => {
        if (!response.ok) {
            location.reload()
        }
    }).then(() => {
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: form.full_name.value.trim(),
                    phone: form.phone_number.value.trim(),
                    email: form.email.value.trim(),
                    address: {
                        line1: form.address_1.value.trim(),
                        line2: form.address_2.value.trim(),
                        city: form.post_town.value.trim(),
                        country: form.country.value.trim(),
                        state: form.county.value.trim(),
                    }
                },
            },
            shipping: {
                name: form.full_name.value.trim(),
                phone: form.phone_number.value.trim(),
                address: {
                    line1: form.address_1.value.trim(),
                    line2: form.address_2.value.trim(),
                    city: form.post_town.value.trim(),
                    country: form.country.value.trim(),
                    postal_code: form.postcode.value.trim(),
                    state: form.county.value.trim(),
                }
            }
        }).then(result => {
            if (result.error) {
                errorDiv.innerHTML = `
                <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                </span>
                <span>${result.error.message}</span>
            `
                card.update({
                    "disabled": false
                })
                paymentButton.removeAttribute("disabled")
            } else {
                if (result.paymentIntent.status === "succeeded") {
                    form.submit()
                }
            }
        })
    })
})