//
//  CircleView.swift
//  Fingers
//
//  Created by Zachary Lahey on 5/9/19.
//  Copyright © 2019 Zachary Lahey. All rights reserved.
//

import UIKit

class CircleView: UIView {
    
    var circleColor = UIColor.blue
    override init(frame: CGRect) {
        super.init(frame: frame)
        self.backgroundColor = UIColor.clear
    }

    required init(coder aDecoder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    func updateColor(color: UIColor){
        circleColor = color
    }

    override func draw(_ rect: CGRect) {
        if let context = UIGraphicsGetCurrentContext() {
            

            context.setLineWidth(5.0);
            

            circleColor.set()
            

            let center = CGPoint(x: frame.size.width/2, y: frame.size.height/2)
            let radius = (frame.size.width - 10)/2
            context.addArc(center: center, radius: radius, startAngle: 0.0, endAngle: .pi * 2.0, clockwise: true)
            

            context.strokePath()
        }
    }
}

class CircleView2: UIView {
    
    var circleColor = UIColor.black
    override init(frame: CGRect) {
        super.init(frame: frame)
        self.backgroundColor = UIColor.clear
    }
    
    required init(coder aDecoder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    func updateColor(color: UIColor){
        circleColor = color
    }
    
    override func draw(_ rect: CGRect) {

        if let context = UIGraphicsGetCurrentContext() {
            
            context.setLineWidth(5.0);
            
            circleColor.set()
            
            let center = CGPoint(x: frame.size.width/2, y: frame.size.height/2)
            let radius = (frame.size.width - 10)/2
            context.addArc(center: center, radius: radius, startAngle: 0.0, endAngle: .pi * 2.0, clockwise: true)
            

            context.strokePath()
        }
    }
}

class CircleView3: UIView {
    
    var circleColor = UIColor.white
    override init(frame: CGRect) {
        super.init(frame: frame)
        self.backgroundColor = UIColor.clear
    }
    
    required init(coder aDecoder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    func updateColor(color: UIColor){
        circleColor = color
    }
    
    override func draw(_ rect: CGRect) {

        if let context = UIGraphicsGetCurrentContext() {
            

            context.setLineWidth(5.0);
            

            circleColor.set()
            

            let center = CGPoint(x: frame.size.width/2, y: frame.size.height/2)
            let radius = (frame.size.width - 10)/2
            context.addArc(center: center, radius: radius, startAngle: 0.0, endAngle: .pi * 2.0, clockwise: true)
            

            context.strokePath()
        }
    }
}
