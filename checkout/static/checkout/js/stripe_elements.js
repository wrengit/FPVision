const stripePublicKey = document.getElementById("id_stripe_public_key").textContent.slice(1, -1)
const clientSecret = document.getElementById("id_client_secret").textContent.slice(1, -1)
const errorDiv = document.getElementById("card-errors")
const form = document.getElementById("payment-form")
const paymentButton = document.getElementById("submit-payment-button")
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
            paymentButton.removeAttribute("disabled")
        } else {
            if (result.paymentIntent.status === "succeeded") {
                form.submit()
            }
        }
    })
})