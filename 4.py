text = "Loremn ipsum dolor sit amet, consectetur adipiscing elit. Morbi eget lacinia augue. Fusce egestas blandit congue. Duis pellentesque, elit in ornare facilisis, ante quam maximus leo, sed luctus arcu enim eu dolor. Quisque odio ipsum, congue ut erat nec, posuere bibendum tortor. Suspendisse suscipit erat lorem, et tristique erat aliquet vitae. Nunc sed dolor at velit faucibus venenatis et vitae tortor. Integer magna enim, eleifend eget quam a, accumsan semper nisi. Pellentesque sed ullamcorper massa. Donec facilisis dapibus justo non ornare. Sed faucibus commodo euismod. Vivamus viverra sem neque, eu congue tortor finibus vel. Suspendisse nec rhoncus ipsum."
result = text.find("nisi")
if result == -1:
    print("Bu kelime bulunamamistir")
elif result != -1:
    print(f"Kelime bulundu. Bas harfinin indexi: {result}")
