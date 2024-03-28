package recursiveart;

import java.awt.*;

import processing.core.PApplet;
/*
 * WHERE IM AT: I have the logic down for the target
 * but for some reason the frame comes up gray. My comp
 * could be running slow but I'm not sure. I tried to make 
 * draw() an object so i could return the recursion but that
 * didn't work. 
 * 
 * TO DO:
 * 
 *  dream catcher logic
 *  squares logic
 *  my own design's logic (maybe a bunch of arcs with the 
 *  stroke changing colors)
 */

public class RecursiveArt extends PApplet {

	/*
	 * The setup sets the initial size, 
	 * adds smoothing (for pixelated lines)
	 * and noStroke, which takes out outlines of shapes.
	 * This method is called once - when the program starts.
	 */
	public void setup() {
		int dimMax = 800;
		size(dimMax, dimMax);
		smooth();
		noStroke();
	}
	
	/*
	 * The draw program is called many times a second.
	 * It draws shapes to the screen.
	 * 
	 * The art should still be correct when the window is resized.
	 */
	public void draw(int n) {
		// Draw background first.
		int white = 255;
		int numTar = 10;
		int midPt = 200;
		int dimHalf = 400;
		
		//MAKE ALL VARIABLES COME FROM A SUPER CLASS
		
		background(white, white, white);
		
		//Drawing the Target
			if (n < numTar){
			ellipseMode(CORNER);
			ellipse(midPt, midPt, dimHalf, dimHalf);
			
				if (n % 2 == 1){
					fill(0, 0, 255);
				}
				else {
					fill(255, 0, 0);
				}
			dimHalf = dimHalf / 10;
			//return draw(n+1);
			}

		// Draw the "dream catcher"

		// Draw the triangles
		
		// Draw whatever you want as long as its recursive.
	}
}
