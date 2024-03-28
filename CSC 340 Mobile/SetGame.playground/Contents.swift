import UIKit

var str = "Hello, playground"

/*
 12 Buttons, Enum, shuffle() [for whats on the cards {tone, shape, num} & to randomize the deck of cards], struct, optional, array
 */

enum Symbol {
    case rock
    case paper
    case scissors
}

enum Shade {
    case dark
    case mid
    case light
}

//enum Count {
//    case one
//    case two
//    case three
//}

struct Card {
    var symbol: Symbol
    var shade: Shade
    var count: Int
    
    var appearance: String{
        var show = ""
        switch symbol{
        case .rock:
            switch shade {
            case .light: show = "✊🏻"
            case .dark: show = "✊🏿"
            case .mid: show = "✊🏽"
            }
        case .paper:
            switch shade {
            case .light: show = "✋🏻"
            case .dark: show = "✋🏿"
            case .mid: show = "✋🏽"
        }
        case .scissors:
            switch shade {
            case .light: show = "✌🏻"
            case .dark: show = "✌🏿"
            case .mid: show = "✌🏽"
    }
}
    }
    
    struct SetGame {
        var deck: [Card]
        var board: [Card]
        
        init(){
            deck = []
        for symbol in [Symbol.rock, .paper, .scissors]{
            for shade in [Shade.dark, .mid, .light]{
                    for count in 1...3 {
                        deck.append(Card(symbol: symbol, shade: shade, count: count))
        }
        }
        }
        deck.shuffle()
            board = []
            for _ in 1...12{
                board.append(deck.popLast()!)
            }
    }
    }


var game = SetGame()
    print("Board: \(game.board.count)")
    for card in game.board {
    print(card.appearance)
    }
    print("Deck: \(game.deck.count)")
for card in game.deck {
    print(card.apperance)
}


    mutating func play(indexes: [Int]){
        if isSet(indexes: indexes){
            for index in indexes{
                board[index] = deck.popLast()
            }
        }
}
