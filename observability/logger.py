class PipelineLogger:
    def __init__(self):
        self.logs = []

    def log(self, step: str, input_data: dict, output_data: dict):
        self.logs.append({
            "step": step,
            "input": input_data,
            "output": output_data,
        })

    def get_logs(self):
        return self.logs