TASK_STATES = {
    0: "Unknown",
    1: "Disabled",
    2: "Queued",
    3: "Ready",
    4: "Running"
}

SUCCESS_ERROR_CODES = {
    0: "The operation completed successfully (often means the task ran without errors).",
    1: "Incorrect function (general failure, often indicating some error but not very specific).",
    2: "The system cannot find the file specified (often means the script or executable could not be found).",
    10: "The environment is incorrect (often means there was an issue with the system environment).",
    267011: "(0x00041303) The task has not yet run.",
    2147750687: "(0x8004131F) The task scheduler service is not available.",
    2147943645: "(0x80070015) The device is not ready.",
    2147942402: "(0x80070002) The system cannot find the file specified."
}