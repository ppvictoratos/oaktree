//
//  ViewController.swift
//  Fingers
//
//  Created by Zachary Lahey on 5/9/19.
//  Copyright © 2019 Zachary Lahey. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet weak var fingersTitle: UILabel!
    @IBOutlet weak var players: UILabel!
    @IBOutlet weak var playerIncrease: UIStepper!
    @IBOutlet weak var gameMode: UISegmentedControl!
    @IBOutlet weak var gameStarter: UIButton!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        
        playerIncrease.autorepeat = true
        playerIncrease.minimumValue = 2
        playerIncrease.maximumValue = 5
    }
    
    @IBAction func stepperValueChange(_ sender: UIStepper) {
        players.text = Int(sender.value).description
    }
    
    override func prepare(for segue: UIStoryboardSegue, sender: Any?) {
        if segue.identifier == "goNextPage"{
            var destinationVC = segue.destination as? SecondViewController
            destinationVC?.numPlayers = Int(playerIncrease.value)
        }
    }
    

}

