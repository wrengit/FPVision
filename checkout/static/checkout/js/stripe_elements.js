let stripePublicKey = document.getElementById("id_stripe_public_key").textContent.slice(1, -1)
let clientSecret = document.getElementById("id_client_secret").textContent.slice(1, -1)
let stripe = Stripe(stripePublicKey)
let elements = stripe.elements()
let card = elements.create("card")
card.mount("#card-element")

card.addEventListener('change', e => {
    let errorDiv = document.getElementById("card-errors")
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

let form = document.getElementById("payment-form")

form.addEventListener("submit", e => {
    let errorDiv = document.getElementById("card-errors")
    e.preventDefault()
    card.update({
        "disabled": true
    })
    document.getElementById("submit-payment-button").setAttribute("disabled", "")
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
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
            document.getElementById("submit-button").removeAttribute("disabled")
        } else {
            if (result.paymentIntent.status === "succeeded") {
                form.submit()
            }
        }
    })
})