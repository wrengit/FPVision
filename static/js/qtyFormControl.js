function qtyFormControl() {
    return {
        handleEnableDisable(targetId) {
            let input = document.getElementById(`qty-${targetId}`);
            let currentVal = parseInt(input.value);
            let maxVal = parseInt(input.getAttribute("max"));
            let minusDisabled = currentVal < 1;
            let plusDisabled = currentVal > maxVal - 1;
            let increment = document.getElementById(`increment-${targetId}`);
            let decrement = document.getElementById(`decrement-${targetId}`);
            if (minusDisabled) {
                decrement.setAttribute("disabled", "");
            } else if (plusDisabled) {
                increment.setAttribute("disabled", "");
            } else {
                increment.removeAttribute("disabled");
                decrement.removeAttribute("disabled");
            }
        },
        updateSubmitForm(targetId) {
            let form = document.getElementById(`basket-quantity-form-${targetId}`);
            let input = document.getElementById(`qty-${targetId}`);
            let currentVal = parseInt(input.value);
            let maxVal = parseInt(input.getAttribute("max"));
            if (currentVal > maxVal) {
                input.value = maxVal;
            }
            form.submit();
        },
        updateInput(targetId) {
            let input = document.getElementById(`qty-${targetId}`);
            let currentVal = parseInt(input.value);
            let maxVal = parseInt(input.getAttribute("max"));
            if (currentVal > maxVal) {
                input.value = maxVal;
            }
            this.handleEnableDisable(targetId)
        },
        removeItem(targetId) {
            let csrfToken = "{{csrf_token}}";
            let url = `/basket/remove/${targetId}/`;
            let data = {
                csrfmiddlewaretoken: csrfToken
            };
            fetch(url, data).then(function () {
                location.reload();
            });
        },
        incrementQty(targetId) {
            let input = document.getElementById(`qty-${targetId}`);
            let currentVal = parseInt(input.value);
            let maxVal = parseInt(input.getAttribute("max"));
            if (input.value < maxVal) {
                input.value = currentVal + 1;
            } else {
                input.value = maxVal;
            }
            this.handleEnableDisable(targetId);
        },
        decrementQty(targetId) {
            let input = document.getElementById(`qty-${targetId}`);
            let currentVal = parseInt(input.value);
            let maxVal = parseInt(input.getAttribute("max"));
            if (input.value > 0 && input.value > maxVal) {
                input.value = maxVal;
            } else if (input.value > 0) {
                input.value = currentVal - 1;
            }
            this.handleEnableDisable(targetId);
        },
        //https://stackoverflow.com/questions/19966417/prevent-typing-non-numeric-in-input-type-number
        blockAlpha($event) {
            if (
                ($event.key.length === 1 &&
                    $event.key !== "." &&
                    isNaN($event.key) &&
                    !$event.ctrlKey) ||
                ($event.key === "." &&
                    $event.target.value.toString().indexOf(".") > -1)
            ) {
                $event.preventDefault();
            }
        },
    };
}