//
//  ViewController.swift
//  doge
//
//  Created by Peter Victoratos on 2/18/19.
//  Copyright © 2019 Peter Victoratos. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet weak var dogeVision: UIImageView!
    @IBOutlet weak var yeetLabel: UILabel!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
    }

    @IBAction func buttonPressed(_ sender: UIButton) {
        dogeVision.image = UIImage(named: "doge")
        yeetLabel.textColor = .black
    }
    
}

