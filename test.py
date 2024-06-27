import qrcode.image.svg
factory = qrcode.image.svg.SvgPathFillImage
svg_img=qrcode.make("hello", image_factory=factory)
svg_img.save("myqr.svg")