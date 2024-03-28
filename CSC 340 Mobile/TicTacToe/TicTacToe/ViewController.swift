//
//  ViewController.swift
//  TicTacToe
//
//  Created by Peter Victoratos on 2/25/19.
//  Copyright © 2019 Peter Victoratos. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    var isXTurn = true
    @IBOutlet var boardButtons: [UIButton]!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        resetBoardButtons()
    }

    func resetBoardButtons() {
        for button in boardButtons{
            button.isEnabled = true
            button.setTitle("", for: .normal)
        }
    }

    @IBAction func resetTapped(_ sender: UIButton) {
        resetBoardButtons()
    }
    
    @IBAction func boardButtonTapped(_ sender: UIButton) {
        let turnText = isXTurn ? "X" : "O"
        
        sender.setTitle(turnText, for: .normal)
        sender.isEnabled = false
        
        isXTurn = !isXTurn
    }
    
}

