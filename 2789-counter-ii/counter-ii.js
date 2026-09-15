/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    var currentValue = init
    const resetValue = init 
    return {
        increment: function(){
            return currentValue = currentValue + 1 
        },
        decrement: function(){
            return currentValue = currentValue - 1
        },
        reset: function(){
            return currentValue = resetValue
        }
    }
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */

