import google.cloud.compute_v1 as compute_v1

def print_images_list(project: str) -> str:
    """
    Prints a list of all non-deprecated image names available in given project.

    Args:
        project: project ID or project number of the Cloud project you want to list images from.

    Returns:
        The output as a string.
    """
    images_client = compute_v1.ImagesClient()
    # Listing only non-deprecated images to reduce the size of the reply.
    images_list_request = compute_v1.ListImagesRequest(
        project=project, max_results=100, filter="deprecated.state != DEPRECATED"
    )
    output = []

    # Although the `max_results` parameter is specified in the request, the iterable returned
    # by the `list()` method hides the pagination mechanic. The library makes multiple
    # requests to the API for you, so you can simply iterate over all the images.
    for img in images_client.list(request=images_list_request):
        print(f" -  {img.name}")
        output.append(f" -  {img.name}")
    return "\n".join(output)


