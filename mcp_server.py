import sys
import json
from client import QFTCircuit

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    req_id = req.get("id")

    if method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "quantum_fourier_transform",
                        "description": "Apply Quantum Fourier Transform to complex statevector amplitudes",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "num_qubits": {"type": "integer"},
                                "amplitudes": {
                                    "type": "array",
                                    "items": {"type": "array", "items": {"type": "number"}}
                                }
                            },
                            "required": ["num_qubits", "amplitudes"]
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        name = params.get("name")
        args = params.get("arguments", {})
        if name == "quantum_fourier_transform":
            qft = QFTCircuit(args["num_qubits"])
            vec = [complex(re, im) for re, im in args["amplitudes"]]
            res = qft.transform(vec)
            out = [[c.real, c.imag] for c in res]
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps({"transformed_amplitudes": out})}]}}
    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

def main():
    for line in sys.stdin:
        if line.strip():
            req = json.loads(line)
            res = handle_request(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
