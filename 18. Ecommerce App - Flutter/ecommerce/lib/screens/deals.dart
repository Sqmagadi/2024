import 'package:flutter/material.dart';

class DealsScreen extends StatelessWidget {
  const DealsScreen({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Deals'),
      ),
      body: Center(
        // Customize the body of the deals screen as needed
        child: const Text('This is the deals screen'),
      ),
    );
  }
}
