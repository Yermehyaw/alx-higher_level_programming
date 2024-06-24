#!/usr/bin/node
/* Modules Imported: undefined */


/**
 * 0-rectangle - creates a rectangle class
 */
class Rectangle {
  /**
   * Rectangle - defines a 2d rectangle shape
   *
   * Attributes (properties):
   *   width(int): width of rectangle
   *   height(int): height of rectangle
   */
  constructor (w, h) {
    /**
      * Constructor method for rectangle class
      *
      * Args:
      *   w(int): width of rectangle
      *   h(int): height of rectangle
      */
    if (width <= 0 || height <= 0)
      return this;
    const width = w;
    const height = h;
    return this;
  }
  print() {
    /**
      * print - prints a rectangle object
      *
      * Args:
      *   undefined
      */
    for (let i = width; i > 0; --i) {
      console.log('X');
      for (let j = height; j > 0; --j) {
	console.log('X');
      }
    }
  }
}
