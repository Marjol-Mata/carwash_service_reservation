fetch(pubKeyUrl)
    .then((result) => { return result.json(); })
    .then((data) => {
      const stripe = Stripe(data.publicKey);

      const btn = document.querySelector("#btn-buy");

      btn.addEventListener("click", (event) => {
          fetch(checkoutSessionUrl)
            .then(r => r.json())
            .then(data => {
                return stripe.redirectToCheckout({ sessionId: data.sessionId });
            }).then(r => console.log("Redirect res:", r));
      });
    });