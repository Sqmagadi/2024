import 'package:flutter/material.dart';
import '../components/category_menu.dart';
import '../components/banner_carousel.dart';
import '../components/deals.dart';
import '../components/featured.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return SingleChildScrollView(
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          // Horizontal menu for categories
          const Padding(
            padding: EdgeInsets.symmetric(vertical: 8.0),
            child: CategoryMenu(),
          ),

          // Banner section
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 8.0, vertical: 4.0),
            child: Container(
              height: 200.0,
              decoration: BoxDecoration(
                image: const DecorationImage(
                  image: AssetImage('assets/images/banner/1.png'),
                  fit: BoxFit.contain,
                ),
                borderRadius: BorderRadius.circular(4.0),
              ),
            ),
          ),

          // Add the BannerCarousel component
          const Padding(
            padding: EdgeInsets.symmetric(vertical: 1.0),
            child: BannerCarousel(),
          ),

          // Add the DealsSection component
          Padding(
            padding: const EdgeInsets.symmetric(vertical: 8.0),
            child: DealsSection(
              deals: [
                Deal(
                  imageUrl: 'assets/images/products/1.jpg',
                  title: 'Deal 1',
                  oldPrice: 19.99,
                  newPrice: 14.99,
                ),
                Deal(
                  imageUrl: 'assets/images/products/2.jpg',
                  title: 'Deal 2',
                  oldPrice: 49.99,
                  newPrice: 39.99,
                ),
                Deal(
                  imageUrl: 'assets/images/products/3.jpg',
                  title: 'Deal 1',
                  oldPrice: 19.99,
                  newPrice: 14.99,
                ),
                Deal(
                  imageUrl: 'assets/images/products/4.jpg',
                  title: 'Deal 1',
                  oldPrice: 19.99,
                  newPrice: 14.99,
                ),
              ],
            ),
          ),

          // Add the FeaturedSection component
          Padding(
            padding: const EdgeInsets.symmetric(vertical: 8.0),
            child: FeaturedSection(
              featuredProducts: [
                FeaturedProduct(
                  imageUrl: 'assets/images/products/1.jpg',
                  title: 'Product 1',
                  price: 39.99,
                ),
                FeaturedProduct(
                  imageUrl: 'assets/images/products/2.jpg',
                  title: 'Product 2',
                  price: 29.99,
                ),
                FeaturedProduct(
                  imageUrl: 'assets/images/products/3.jpg',
                  title: 'Product 3',
                  price: 29.99,
                ),
                FeaturedProduct(
                  imageUrl: 'assets/images/products/4.jpg',
                  title: 'Product 4',
                  price: 29.99,
                ),
                // Add more FeaturedProduct objects as needed...
              ],
            ),
          ),

          // Add other sections such as featured products, promotions, etc.
        ],
      ),
    );
  }
}
