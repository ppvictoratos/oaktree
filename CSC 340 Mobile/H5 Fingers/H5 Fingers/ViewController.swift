//
//  ViewController.swift
//  H5 Fingers
//
//  Created by Peter Victoratos on 4/24/19.
//  Copyright © 2019 Loveshack Enterprises. All rights reserved.
//
//  Alters finger touch circles' attributes and changes the background based upon which
//  game is selected. Tells the model which game is selected.

import UIKit

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
    }
    
    var num = 2
    @IBOutlet weak var ParticipantLabel: UILabel!
    @IBOutlet weak var SegmentedControl: UISegmentedControl!
    //Model Model = new Model()
    
    //Connects to the model so it can alter the rules
    @IBAction func SegmentChanged(_ sender: UISegmentedControl) {
        //Model.mode = false
        //Model.participants = num
    }

    //Sets the value of the participants
    @IBAction func Stepper(_ sender: UIStepper) {
        num = Int(sender.value)
        ParticipantLabel.text = String(num)
    }

}

