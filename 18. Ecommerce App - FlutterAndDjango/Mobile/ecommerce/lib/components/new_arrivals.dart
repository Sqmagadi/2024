import 'package:ecommerce/screens/new_arrivals.dart';
import 'package:flutter/material.dart';
// import '../screens/deals.dart';
import '../screens/product_details.dart';
import '../models/product_model.dart';



const int maxNameLength = 20;

class NewArrivalSection extends StatelessWidget {
  // final List<Deal> deals;
  final List<Product> products; // Add a list of Product objects

  const NewArrivalSection({Key? key, required this.products})
      : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(8.0),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          // Section title row
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 8.0),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                // Section title
                Text(
                  'New Arrivals',
                  style: Theme.of(context).textTheme.titleLarge,
                ),
                // "See More" button and icon
                Row(
                  children: [
                    TextButton(
                      onPressed: () {
                        // Navigate to the DealsScreen
                        Navigator.push(
                          context,
                          MaterialPageRoute(
                            builder: (context) => const NewArrivalScreen(),
                          ),
                        );
                      },
                      child: const Text('See More'),
                    ),
                    const Icon(
                      Icons.keyboard_double_arrow_right,
                      size: 16.0,
                      color: Colors.grey,
                    ),
                  ],
                ),
              ],
            ),
          ),
          // Horizontally scrolling list of deals
          SizedBox(
            height: 180, // Adjust height as needed
            child: ListView.builder(
              scrollDirection: Axis.horizontal,
              itemCount: products.length,
              itemBuilder: (context, index) {
                final newProduct = products[index];
                // Find the associated Product object using the deal title or other identifying properties
                final product = products.firstWhere(
                  (product) => product.name == newProduct.name,
                  orElse: () => throw Exception('No matching Product found'),

                  // Handle the case when no matching product is found
                );

                // Only pass the product if it was found
                // ignore: unnecessary_null_comparison
                if (product != null) {
                  return NewArrivalItem(product: product);
                }
                // Otherwise, return an empty container or some other placeholder
                return Container();
              },
            ),
          ),
        ],
      ),
    );
  }
}

class NewArrivalItem extends StatelessWidget {
  final Product product;

  const NewArrivalItem({Key? key, required this.product})
      : super(key: key);

  @override
  Widget build(BuildContext context) {
    // Truncate product name if it exceeds the maximum length
    String truncatedName = product.name.length > maxNameLength
        ? '${product.name.substring(0, maxNameLength)}...'
        : product.name;
    return GestureDetector(
      onTap: () {
        // Navigate to the ProductDetailsScreen when the deal item is clicked
        Navigator.push(
          context,
          MaterialPageRoute(
            builder: (context) => ProductDetailsScreen(product: product),
          ),
        );
      },
      child: Padding(
        padding: const EdgeInsets.symmetric(horizontal: 4.0),
        child: Card(
          elevation: 2.0,
          shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(8.0),
          ),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              // Deal image
              ClipRRect(
                borderRadius: const BorderRadius.vertical(top: Radius.circular(8.0)),
                child: Image.network(
                  product.image,
                  height: 100.0,
                  width: 100,
                  fit: BoxFit.contain,
                  semanticLabel:
                      product.name, // Add semantic label for accessibility
                ),
              ),

              // Deal details
              Padding(
                padding: const EdgeInsets.all(8.0),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    // Deal title
                    Text(
                      truncatedName,
                      style: Theme.of(context).textTheme.titleSmall,
                    ),
                    const SizedBox(height: 4.0),
                    // Deal prices
                    Row(
                      children: [
                        // Old price (struck through)
                        Text(
                          '\$${product.price.toStringAsFixed(2)}',
                          style: const TextStyle(
                            color: Colors.grey,
                            decoration: TextDecoration.lineThrough,
                          ),
                        ),
                        const SizedBox(width: 8.0),
                        // New price (highlighted)
                        Text(
                          '\$${product.salePrice.toStringAsFixed(2)}',
                          style: const TextStyle(
                            color: Colors.red,
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                      ],
                    ),
                  ],
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
