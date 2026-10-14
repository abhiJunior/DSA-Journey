/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = function(functions) {
    return new Promise((resolve, rejected)=>{
        const results = []
        const total = functions.length
        let completed = 0
        for (let i = 0; i < functions.length; i += 1){
            functions[i]()
                .then((value)=>{
                    results[i] = value
                    completed += 1
                    if (completed === total) {
                        resolve(results);
                    }
                })
                .catch((error)=>{
                    rejected(error)
                })
        }
    })
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */