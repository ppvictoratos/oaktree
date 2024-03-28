//
//  SecondViewController.swift
//  Fingers
//
//  Created by Zachary Lahey on 5/9/19.
//  Copyright © 2019 Zachary Lahey. All rights reserved.
//

import UIKit

class SecondViewController: UIViewController {
    
    @IBOutlet weak var image: UIImageView!
    
    var touchCounter = 0
    var numPlayers = 0
    var finalStage = false
    var labelTouches: [CircleView:UITouch] = [:]
    var circles: [CircleView] = []
    var circleCopies: [CircleView:Circle] = [:]
    override func viewDidLoad() {
        super.viewDidLoad()
        view.isMultipleTouchEnabled = true
    }
    
    override func touchesBegan(_ touches: Set<UITouch>, with event: UIEvent?) {
        if (touchCounter < numPlayers){
            print(numPlayers)
            print(touchCounter)
            for touch in touches {
                // Set the Center of the Circle
                // 1
                let circleCenter = touch.location(in: image)
                
                // Set a random Circle Radius
                // 2
                let circleWidth = CGFloat(100)
                let circleHeight = circleWidth
                
                // Create a new CircleView
                // 3
      
                let circleView = CircleView(frame: CGRect(x: circleCenter.x, y: circleCenter.y, width: circleWidth, height: circleHeight))
                var newCirc = Circle(x: Double(circleCenter.x), y: Double(circleCenter.y), width: Double(circleWidth), height: Double(circleWidth))
                view.addSubview(circleView)
                labelTouches[circleView] = touch
                circleCopies[circleView] = newCirc
                circles.append(circleView)
                touchCounter = touchCounter + 1
            }
        }
        if(touchCounter == numPlayers){
            touchesComplete()
        }
        if(finalStage==true){
            finalHighlight()
        }
    }

    override func touchesMoved(_ touches: Set<UITouch>, with event: UIEvent?) {
        if(self.finalStage != true){
            updateUI()
        }
    }
    
    override func touchesEnded(_ touches: Set<UITouch>, with event: UIEvent?) {
        terminateTouches(touches)
    }
    
    override func touchesCancelled(_ touches: Set<UITouch>, with event: UIEvent?) {
        terminateTouches(touches)
    }
    
    func terminateTouches(_ touches: Set<UITouch>) {
        for touch in touches {
            for circle in circles {
                if labelTouches[circle] == touch {
                    labelTouches[circle] = nil
                    break
                }
            }
        }
        updateUI()
    }
    
    func updateUI() {
        
        for (num, touch) in labelTouches {
            num.center = touch.location(in: view)
            circleCopies[num]!.x = Double(num.center.x)
            circleCopies[num]!.y = Double(num.center.y)
        }
        
    }
    
    func touchesComplete(){
        self.view.backgroundColor = UIColor.yellow
        DispatchQueue.main.asyncAfter(deadline: .now()+3){
            self.finalStage = true
        }
    }
    func finalHighlight(){
        self.view.backgroundColor = UIColor.black
        var it = circles[Int.random(in:0..<numPlayers)]

        for (num, newCirc) in circleCopies{
                if (num == it) {
                    var newCircle = CircleView2(frame: CGRect(x: circleCopies[num]!.x, y: circleCopies[num]!.y, width: circleCopies[num]!.width, height: circleCopies[num]!.height))
                    view.addSubview(newCircle)
                }
                else{
                    var newCircle = CircleView3(frame: CGRect(x: circleCopies[num]!.x, y: circleCopies[num]!.y, width: circleCopies[num]!.width, height: circleCopies[num]!.height))
                    view.addSubview(newCircle)
                }
        }

    }
}

struct Circle{
    var x: Double
    var y: Double
    var width:Double
    var height: Double
}
