import win32com.client

class FolderManager:
    def __init__(self, scheduler_client):
        self.scheduler = scheduler_client

    def create_folder(self, folder_name: str, parent_folder: str | None="\\"):
        """Create a folder under the parent folder.
        
        Parameters:
            parent_folder (`str`): Where the new folder will live under.
            folder_name (`str`): Name for the new folder.

        """
        root = self.scheduler.GetFolder(parent_folder)
        if folder_name not in [f.Name for f in root.GetFolders(0)]:
            raise ValueError(f"Could not find {folder_name} in task scheduler.")
        else:
            root.CreateFolder(folder_name)

    def delete_folder(self, folder_name: str, parent_folder: str | None="\\"):
        """Delete a folder under the parent folder.
        
        Parameters:
            parent_folder (`str`): Where the new folder will live under.
            folder_name (`str`): Name for the new folder.

        """
        root = self.scheduler.GetFolder(parent_folder)

        if folder_name in [f.Name for f in root.GetFolders(0)]:
            root.DeleteFolder(folder_name)

    
